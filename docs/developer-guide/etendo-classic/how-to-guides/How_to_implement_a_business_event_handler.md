![](skins/openbravo/images/social-blogs-sidebar-banner.png){: .legacy-image-style}

######  Toolbox

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Main Page  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Upload file  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} What links here  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Recent changes  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Help  
  
  

######  Search

######  Participate

![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Communicate  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Report a bug  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Contribute  
![](skins/openbravo/images/flecha1.jpg){: .legacy-image-style} Talk to us now!  

  

#  How to implement a business event handler

##  Contents

  * 1  Introduction 
  * 2  Example Module 
  * 3  The event handler - a first implementation 
    * 3.1  Result 
    * 3.2  Event methods 
    * 3.3  Filtering only relevant events 
  * 4  The event handler - adding some business logic 
    * 4.1  Changing the entity on update/insert 
    * 4.2  Adding a child instance 
    * 4.3  Interrupt the save action 
  * 5  Examples of business entity event handlers 

  
---  
  
##  Introduction

The  business entity event  allows you to implement business logic which
reacts to specific events which are fired when entities are updated, deleted
or inserted into the database. Business entity events correspond to triggers
in the database. The main advantage of implementing logic using business
entity events instead of in triggers is that you can code your logic in java
using your IDE. This helps productivity and quality as you can code, debug and
test in an integrated environment with the rest of your business logic.

Some notes on business entity events:

  * they are fired when an entity instance is updated, deleted or inserted. Before the actual operation has been done in the database, so you can change or add information which is persisted together with the event entity. 
  * your event handling code runs in the same transaction as the business event, changes you make to the database are persisted together with the business entity event in one transaction. 
  * you can make use of the full  data access layer  functionality in your event handling code, you can query, create new objects, persist etc. 
  * Business entity events **only** work when accessing the database through the data access layer, so they do **not** work for classic windows or direct jdbc calls! 

Business events make use of the event framework provided by the  Weld
framework. To register an event handler we will use annotations. Weld
automatically analyzes the classpath and automatically detect classes/methods
with annotations. Note that to maximize performance certain part of the
classpath are excluded, check out  this section  if your event handlers are
not found.

In this HowTo we will be implementing an event handler on the Greeting entity.
Whenever a title get's saved we will add a spanish translation. In addition we
will print some messages to the console for other business events.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_business_event_handler-0.png){: .legacy-image-style}

##  Example Module

This howto is supported by an example module which shows example of the code
shown and discussed in this howto.

The code of the example module can be downloaded from this mercurial
repository:
https://code.openbravo.com/erp/mods/org.openbravo.client.application.examples/

The example module is available through the Central Repository (See 'Client
Application Examples'), for more information see the  Examples Client
Application  project page.

The complete source code of the event handler is available  here  .

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |  The
example module also contains implementations of other howtos.  
---|---  
  
##  The event handler - a first implementation

An event handler is implemented as a normal java class in your module. The key
thing is to create methods with an annotation on the parameters. Here is a
first simple example of an event handler which listens to events on the
Greeting entity:

    
    
    class GreetingEventHandler extends EntityPersistenceEventObserver {
      private static Entity[] entities = { ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
      private static final Logger logger = LogManager.getLogger();
     
      @Override
      protected Entity[] getObservedEntities() {
        return entities;
      }
     
      public void onUpdate(@Observes EntityUpdateEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        logger.info("Greeting " + event.getTargetInstance().getId() + " is being updated");
      }
     
      public void onSave(@Observes EntityNewEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        logger.info("Greeting " + ((Greeting) event.getTargetInstance()).getName()
            + " is being created");
      }
     
      public void onDelete(@Observes EntityDeleteEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        logger.info("Greeting " + event.getTargetInstance().getId() + " is being deleted");
      }
    }

Note:

  * it makes sense to extend the  EntityPersistenceEventObserver  , it helps to filter for the correct events. 
  * the name of the method is not relevant, the relevant thing is the annotation on the parameter and the parameter. Weld uses this to detect and register for which events this class listens 
  * the eventhandler will be called for events occurring on all entities, therefore each method starts with the if statement with isValidEvent, to filter out unwanted events. 
  * the use of the _org.apache.logging.log4j.Logger_ class is recommended for logging as shown above 

![](/assets/developer-guide/etendo-classic/how-to-guides/Bulbgraph.png){: .legacy-image-style} |
Starting from **3.0PR19Q2** classes extending _EntityPersistenceEventObserver_
are defined as _@ApplicationScoped_ by default. See [  here  ] for additional
information.  
---|---  
  
###  Result

When you add the above class to your module and restart the system and then go
to the greeting window:

http://localhost:8080/openbravo/?tabId=282

And do some actions you should see the following messages in the console:

Greeting FF8081813097E041013097E805F4000F is being updated

Greeting FF8081813097E041013097E805F4000F is being deleted

Greeting Mr is being created

###  Event methods

The source code above illustrates how the event methods are implemented:

    
    
     
      public void onUpdate(@Observes EntityUpdateEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        logger.info("Greeting " + event.getTargetInstance().getId() + " is being updated");
      }
     
      public void onSave(@Observes EntityNewEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        logger.info("Greeting " + ((Greeting) event.getTargetInstance()).getName()
            + " is being created");
      }
     
      public void onDelete(@Observes EntityDeleteEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        logger.info("Greeting " + event.getTargetInstance().getId() + " is being deleted");
      }

Notes:

  * you only need to implement a method for the event you want to listen to, so if you only need to listen to update events then only implement a method with the @Observes EntityUpdateEvent parameter. 
  * each method starts with a check if the event is valid, this is needed to filter for relevant events only, see the section below. 
  * within the event handler methods you can use the api on the event object to detect which is the entity event and to get access to the current and previous state of the entity. See  here  for more information. 

###  Filtering only relevant events

As mentioned above, the event methods get called for all entities of all
types. In our example we only want to handle events on the Greeting entity.
There is specific code in the example above which takes care of this. It
starts in the top of the class:

    
    
      private static Entity[] entities = { ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME) };
     
      @Override
      protected Entity[] getObservedEntities() {
        return entities;
      }

The getObservedEntities method is called when you call the isValidEvent
method, getObservedEntities returns the entities you want to handle in this
event handler. To make use of it add this code to each event handling method
in the beginning:

    
    
        if (!isValidEvent(event)) {
          return;
        }

This part is needed because the event methods will be called for entities of
all types. In this example we only want to listen to changes on the Greeting
entity.

##  The event handler - adding some business logic

In this next step we will be adding logic to the event handler:

  * whenever a greeting gets created/updated, add a . to the title if it was not already there 
  * when a new greeting gets created, add a translation for it. 

    
    
    to create a new translation for when a new greeting is added. For this example we will be adding a dutch translation. 
    

###  Changing the entity on update/insert

In this step we will be adding some simple logic to the update and save event
to add a dot to the title if it not already has one.

    
    
      public void onUpdate(@Observes EntityUpdateEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        final Greeting greeting = (Greeting) event.getTargetInstance();
        final String title = greeting.getTitle();
        if (title != null && !title.endsWith(".")) {
          final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
          final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
          // note use setCurrentState and not setters on the Greeting object directly
          event.setCurrentState(greetingTitleProperty, title + ".");
        }
        logger.info("Greeting " + event.getTargetInstance().getId() + " is being updated");
      }
     
      public void onSave(@Observes EntityNewEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        final Greeting greeting = (Greeting) event.getTargetInstance();
        // now also add the dot to the title
        final String title = greeting.getTitle();
        if (title != null && !title.endsWith(".")) {
          final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
          final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);
          // note use setCurrentState and not setters on the Greeting object directly
          event.setCurrentState(greetingTitleProperty, title + ".");
        }
     
        logger.info("Greeting " + ((Greeting) event.getTargetInstance()).getName()
            + " is being created");
      }

Let's walk through the code. First cast the instance and get the title:

    
    
        final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
        final String title = greeting.getTitle();

If the title does not end on a dot then get the entity and the relevant
property:

    
    
     
        if (title != null && !title.endsWith(".")) {
          final Entity greetingEntity = ModelProvider.getInstance().getEntity(Greeting.ENTITY_NAME);
          final Property greetingTitleProperty = greetingEntity.getProperty(Greeting.PROPERTY_TITLE);

Note that we use the generated constants to the entity name and property
names, this gives compile time checking and is a recommended practice.

And then set the current state (note: don't call setters on the Greeting
instance itself, this does not work because when the event has been
broadcasted, Hibernate has already read the state of the object. So you must
change the value through the special setCurrentState method:

    
    
          event.setCurrentState(greetingTitleProperty, title + ".");

The changed entity instance does not need to be saved explicitly, this is done
by the  data access layer  and hibernate automatically.

Then test the changes, go to the window (
http://localhost:8080/openbravo/?tabId=282  ), enter a new greeting without a
dot in the title. When saving you will see a dot getting added. Try updating
the record, you will have the same behavior.

###  Adding a child instance

As the next step we will be adding logic to the onSave method to create an
extra child instance (a new translation). This is a bit more complex. Add the
following code to the onSave method at the end:

    
    
        final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
        // set relevant translation properties
        greetingTrl.setGreeting(greeting);
        // 171 is dutch, choose any other language..
        greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
        // note we can call getters on the targetInstance, but not setters!
        greetingTrl.setName(greeting.getName());
        greetingTrl.setTitle(greeting.getTitle());
        greetingTrl.setTranslation(false);
     
        // and add the greetingTrl to the greeting
        // we don't use event.setCurrentState as we get the list and add to it
        // get the trl property for the greeting entity
        final Property greetingTrlProperty = greetingEntity
            .getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
        @SuppressWarnings("unchecked")
        final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
        greetingTrls.add(greetingTrl);
     
        // don't need to save the greetingTrl, it is saved as the child of the greeting
        // OBDal.getInstance().save(greetingTrl);

Let's walk through the code. First the trl object is created and some
properties are set. Note as the object is not part of the event you can call
its setters directly. The language is arbitrarily chosen. See the  DAL
document for information on the api's you can use to retrieve objects from the
database.

    
    
        final GreetingTrl greetingTrl = OBProvider.getInstance().get(GreetingTrl.class);
        // set relevant translation properties
        greetingTrl.setGreeting(greeting);
        // 171 is dutch, choose any other language..
        greetingTrl.setLanguage(OBDal.getInstance().get(Language.class, "171"));
        // note we can call getters on the targetInstance, but not setters!
        greetingTrl.setName(greeting.getName());
        greetingTrl.setTitle(greeting.getTitle());
        greetingTrl.setTranslation(false);

Then as a next step add the new trl object to the event entity. This is a bit
special as we need to update a List property of the event entity. So instead
of calling setCurrentState we get the list and add to it. This is a correct
way of doing this:

    
    
        // and add the greetingTrl to the greeting
        // we don't use event.setCurrentState as we get the list and add to it
        // get the trl property for the greeting entity
        final Property greetingTrlProperty = greetingEntity
            .getProperty(Greeting.PROPERTY_GREETINGTRLLIST);
        @SuppressWarnings("unchecked")
        final List<Object> greetingTrls = (List<Object>) event.getCurrentState(greetingTrlProperty);
        greetingTrls.add(greetingTrl);
     
        // don't need to save the greetingTrl, it is saved as the child of the greeting
        // OBDal.getInstance().save(greetingTrl);

The trl object is a child of the Greeting event entity and will be persisted
together with it, so you don't need to explicitly save it.

When you now enter a new entry in the window, you will see an additional
translation child record being created.

  

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_to_implement_a_business_event_handler-3.png){: .legacy-image-style}

###  Interrupt the save action

Sometimes you need to interrupt the save action because the user are doing
something wrong, this can be done throwing an exception

    
    
     
      public void onUpdate(@Observes
      EntityUpdateEvent event) {
        if (!isValidEvent(event)) {
          return;
        }
        final OBSA_Orderline_Assign olineAssign = (OBSA_Orderline_Assign) event.getTargetInstance();
        if (olineAssign.getProductWithStorage().getProduct() != olineAssign.getSalesOrderLine()
            .getProduct()) {
          String language = OBContext.getOBContext().getLanguage().getLanguage();
          ConnectionProvider conn = new DalConnectionProvider(false);
          throw new OBException(Utility.messageBD(conn, "OBSA_ErrorProduct", language));
        }
      }
     

##  Examples of business entity event handlers

Openbravo uses business entity event handlers to implement business logic in
various locations, here are some examples:

  * ModuleHandler 
  * SetDocumentNoHandler 

The complete source code of the example event handler is available  here  .

Retrieved from "
http://wiki.openbravo.com/wiki/How_to_implement_a_business_event_handler  "

This page has been accessed 43,707 times. This page was last modified on 1
February 2019, at 11:55. Content is available under  Creative Commons
Attribution-ShareAlike 2.5 Spain License  .

  
**

Category  :  HowTo

**

