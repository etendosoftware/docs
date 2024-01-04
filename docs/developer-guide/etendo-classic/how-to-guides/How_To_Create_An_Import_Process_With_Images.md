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

  

#  How To Create An Import Process With Images

**Languages:** |

** English  ** |  Translate this article...  
  
---|---  
  
##  Contents

  * 1  Objective 
  * 2  Execution Steps 
    * 2.1  Installing Required Modules 
    * 2.2  Preparing SampleProductsProcess.java 
    * 2.3  Registering the Process 
    * 2.4  Importing the Data 
  * 3  Result 

  
---  
  
##  Objective

The objective of this article is to show you how to make a massive image
importation process. Specificilly, we are going to import product images.

##  Execution Steps

We are going to create a  custom importation process  , using the **Initial
Data Load for Java** module. We are going to use the java class
SampleProductsProcess, included in this module... For that we will use the
java class **SampleProductsProcess.java** as the base that is included in the
**Initial Data Load Module for Java** , and through a series of single
modifications we will include a new column within the import .csv that will
allow us to specify the path of the image that is associated to the product.

###  Installing Required Modules

  * Activate the Professional subscription License. 
  * Go to General Setup -> Application -> Module Management -> Add Modules 
  * Search and install the following modules. 
    * Initial Data Load (Refer [  [1]  ]) 
    * Initial Data Load Extension for Java (Refer[  [2]  ]) 

###  Preparing SampleProductsProcess.java

The following modifications need to be made:

  * **getEntityName** method: We will simply return the name of our new entity. 

    
    
    
    public String getEntityName() {
        return "Simple Products With Image";
    }

  * **getParameters** method : We add a new parameter to localize our image. 

    
    
    
        ....
        new Parameter("ImageLocation", Parameter.STRING) };
        ....

  * **validateProcess** method: We add a validator for our new field (for example: for the maximum length) 

    
    
    
        ....
        validator.checkString(values[21], 255);
        ....

  * **internalProcess** method: We have to pass a parameter to the createProduct() method. 

    
    
    
    public BaseOBObject internalProcess(Object... values) throws Exception {
        return createProduct((String) values[0], (String) values[1], (String) values[2],
            (String) values[3], (String) values[4], (String) values[5], (String) values[6],
            (String) values[7], (String) values[8], (String) values[9], (String) values[10],
            (String) values[11], (String) values[12], (String) values[13], (String) values[14],
            (String) values[15], (String) values[16], (String) values[17], (String) values[18],
            (String) values[19], (String) values[20], (String) values[21]);
    }

  * **createProduct** method: Additionally to receiving a new parameter (imagelocation), this method does contain the logic to import the image to the database from its physical location. 

    
    
    
        ....
        File imageFile = new File(imagelocation);
        if (imageFile.exists()) {
          FileInputStream is = new FileInputStream(imageFile);
          long length = imageFile.length();
          byte[] bytes = new byte[(int) length];
          int offset = 0;
          int numRead = 0;
          while (offset < bytes.length 
             && (numRead = is.read(bytes, offset, bytes.length - offset)) >= 0) {
              offset += numRead;
          }
          is.close();
          ByteArrayInputStream bis = new ByteArrayInputStream(bytes);
          BufferedImage rImage = ImageIO.read(bis);
          Image productImage = OBProvider.getInstance().get(Image.class);
          productImage.setName(imageFile.getName());
          productImage.setBindaryData(bytes);
          productImage.setWidth(new Long(rImage.getWidth()));
          productImage.setHeight(new Long(rImage.getHeight()));
          productImage.setMimetype(tika.detect(bytes));
          OBDal.getInstance().save(productImage);
          OBDal.getInstance().flush();
          product.setImage(productImage);
        }
        ....

###  Registering the Process

  * Go to Master Data Management -> Initial Data Load -> Setup -> Entity Default Value 
  * Register your Java file here as shown in the screen shot. 

|

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-0.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-1.png){: .legacy-image-style}

View larger

|  
---|---|---  
  
###  Importing the Data

The .csv file that contains the data, must include the new column we have
added, with the string **"ImageLocation"** in the header.

|

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-2.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-3.png){: .legacy-image-style}

View larger

|  
---|---|---  
  
Pay special attention on the class name while adding the entity default value.

  * Import the data using import window 
  * Go to Master Data Management -> Initial Data Load -> Process -> Import 
  * Choose the input file 
  * Choose the entity as **"Product With Image"**

|

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-4.png){: .legacy-image-style}

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-5.png){: .legacy-image-style}

View larger

|  
---|---|---  
  
  * Validate the input file. If the file has invalid data, it will show the invalid data in the log.Screen 

![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-6.png){: .legacy-image-style}

  * Once the input values are validated, the data can be loaded into the actual table by clicking on the process. 
  * If there are any issues while processing the input data, appropriate messages will be logged in the message box provided under the Log header in the import screen. 

##  Result

As the result, we have the product imported with its corresponding product
image.  ![](/assets/developer-guide/etendo-classic/how-to-
guides/How_To_Create_An_Import_Process_With_Images-7.png){: .legacy-image-style}

Retrieved from "
http://wiki.openbravo.com/wiki/How_To_Create_An_Import_Process_With_Images  "

This page has been accessed 6,552 times. This page was last modified on 21 May
2013, at 14:18. Content is available under  Creative Commons Attribution-
ShareAlike 2.5 Spain License  .

  
**

Categories  :  Templates  |  HowTo

**

