---
title: Etendo Advanced Security
hide:
    - navigation
---

!!! info
    To be able to include this functionality, the Platform Extensions Bundle must be installed. To do that, follow the instructions from the marketplace: [_Platform Extensions Bundle_](https://marketplace.etendo.cloud/#/product-details?module=5AE4A287F2584210876230321FBEE614){target="\_blank"}.

The **Etendo Advanced Security** module allows the user to customize several security features such as the following:

- Password Security
- Password History
- User Lockout
- Multiple Session Verification
- Changing Password after Login
- Expiration Time (Autolock Password)

!!! info
    For more information about the module configuration visit the [Technical Documentation](/docs/developer-guide/etendo-classic/bundles/platform-extensions-bundle/#etendo-advanced-security).

### **Password Security**

This functionality is executed when the password is changed, either because the user needs to change it or because the system requires it. The process can be done from the **Change Password** field in the navigation bar and/or from the **User** window.

From the **Change Password** process, Etendo will ask for the current password and the new one to make the change. After clicking on **Apply,** a series of checks will be verified to finally execute the corresponding changes.

![](/docs/assets/drive/sQNqx26cwCGfPld7D47SHw_QnmdO5-zHlJ41yN28V3yKv95xq6PMGqHobkKuh8rQa11RNvI6bMpkWMk9k0H6P_n8DilZ0NfQ56yjBZYaP85WyQWXC7shoMt7zU6nxO-3-JMUXzwRJ2ASii0YDJpUN6s.png)

!!! info
    The password must be no less than 8 characters long and its structure must contain at least three of the following characters: letters, uppercase letters, lowercase letters, numbers and symbols.

If the new password does not comply with the above mentioned conditions, a popup appears with an error message indicating the conditions to be fulfilled.

![](/docs/assets/drive/shTQdtbDJq_FrCieCra0q6YLlv5akL6vFAS2Xr9sogzi6IMddd-qi9HJDwKKhxY0fCqpUfcFa-l0agc03ypnwtH_eFpDR6SLWNPVi4edc--fKnZsuzeFwnNC_ITWGd5q07zMCr1ImePmG5cOLmSH_rQ.png)

This process can also be executed from the **User** window by applying the same password requirements mentioned above.

![](/docs/assets/drive/JNG3VeVWDWewBfz_iijE7kUBTZBV-8DUBQAWaiEa1uyxhOxYZxmbC_bavwTW85z0LJ_S9ibzN1XVz8pGIZQZz675KBO8H8vaO1LJ8BXxO3Sl5AOqOvOV2hgDKjMObk6CWCpmB8ChETBvqkEICBJ0SI4.png)

**Etendo Advanced Security** verifies the changes, and if the new password does not fulfill the required conditions, Etendo shows an error message at the moment of registering the changes.

![](/docs/assets/drive/jUjckeZt5RPHdHYZcD0xN9BXUkKoNLOYPrkLIkG4pyqPJBYvFFtkWWKBzgy3pZ2Qr1M-kGZPzd2YXiNxOuOlNdVj26PDen8jOxw-44zBzZsX1G3eNTiIzIHidjO8eiDmrY-uU-XhkUxG2RiUbahRbbQ.png)

### **Password History**

When changing the password, one of the conditions to be fulfilled is that the new password cannot be the same as a previously used one. Etendo creates records of the previously used passwords so, if the user enters a previously used one, the system informs with an **error message.**

This security feature can be configured only with **System Administrator permissions**. To do this, go to the **System Info** window, within the group field **Password Security**, and check the field called **Enable Password History**, according to your preference.

![](/docs/assets/drive/s0Xj63FWSlAuip3ZzJB0OWyHiF-cM8zs8EruyfZEM7qA3Pt1hvcNZkRDHWzSb9t3GkzqrqbRwIuP5hghTfyal4441tIbtMQrNyu1CPQmhLOwJkM1EcQ85tEz5TDRbOQazN15k5hzX-b6NyleAak3u1s.png)

When the configuration of the feature **Password Security** is active and the user **changes the password** to a previously used one, Etendo will show an **error message** explaining the failure in saving the password.

![](/docs/assets/drive/x4qql4v3biKPnkWDrD86UUS4mJkw0HuajIK5AmXZKT0OKjP5LdGjzhtd6L8BkkPsR-a9duOtg9uK6OHWjJbig-vSHrltxOd2TfjU5-_lwfH74sKnuekNk4A-heIRIniDxvEb5F45Ms0SxKbRQdy-ztg.png)

The following example shows the same error message when changing the password from the **Change Password** process.

![](/docs/assets/drive/1VTtHPNlLr0N3fvL1vVQ7FO2lzWcQti5I.png)

!!! info
    Etendo also allows entering the same password an indefinite number of times. In case the user wishes to maintain the same password, just keep the field **Enable Password History** from the System Info window **unchecked**. 

### **User Lockout** 

Another feature of this module is the **blocking** of the user after N number of **unsuccessful login attempts**. When entering a wrong password, Etendo shows an error message indicating the number of attempts left.

In this example, the system shows that there is one attempt left.

![](/docs/assets/drive/C-pmD7RKuMzM6e1fSFHSwLWAusC2cL1U9gKlvxWxe7VRa64uuLwaQ7dm4Cmi_Z773XQsfFzfSPrdfMGDNdnNgKPuWobU4xTlxFtOirr34LPiLMT9bI3LONLsmydtloKyd48GYi_1hRnovcHduVsDwGE.png)

Even if in the next attempt the user is not able to log in correctly, Etendo leaves another message indicating that the user has been blocked.

![](/docs/assets/drive/e_vXv3RF7iceBBddpDNUMwewnLYcr5W7LzjhyzrUMPnGe6oT9v9TeXiGc-8MLQpF_Xv1POEZdvMmIRL5bwfai6-hfaEirW4IKlsrBVzcLndzbtRTYeO0_fwou-fTO00rxDtw2lJJi7LY5LoW7vWPEb8.png)

!!! info
    By default, Etendo configures five attempts to enter the right password. 

To configure the number of unsuccessful login attempts, it is necessary to create a preference from the **Preference** window. In the **Value** field, add the desired number of login attempts, and also select the preference **Maximum number of password attempts** from the **Property** field.

![](/docs/assets/drive/5nXDi_OVP9kEESFxQsu1DJywuIEhpJfGl7UvWYPV4UO1CkEhcs2aXMQQIt51lJrww8TfMAUWMfjky2zRtpqhzzdsYygdDt8VhJAe0HNHAWpFbbTbX7c0khUaD9Dn9so89idLPpfmVAqR9bVfS4h4IAU.png)

!!! warning
    It is important to note that once the new password has been entered, if the user enters again a wrong password, the system will automatically block the login at the first try. 

### **Multiple Session Verification**  

Another functional innovation that facilitates this module is the ability to allow or block to have multiple sessions opened from another browser.

From the **User** window, within the **More Information** field, it is possible to configure the check that allows having several sessions active at the same time. The check is called **Allow multiple sessions**.

![](/docs/assets/drive/vcMT58GIgiB2QsZcR-bt5xyajWgf9isk7sxrFJuwkUW27BKnmLIjcb2YZIEJUB-YE-scGv_n3rZ1jTwKGKwLumx4KAIjSp0SsN1jK4saZNChsH8q2JRn5RS3Q6TkXVdVLa1r7C5wXTPmrfVkJyChjRA.png)

In case the user just wants one session allowed to be activated, uncheck the **Allow multiple sessions** checkbox from the **User** window and, **only with System Administrator permissions**, check the **Enable single session verification** field in the **Session Security** field from the **System Info** window.

![](/docs/assets/drive/Prfolo_qyMafrXpr9dUe_ASCkalv-LjArCWEcMCPSWWi2IzyypsQytDTUlSeMgq_mSbgCYKtebK9aawUzMNotE2V25Lg-RrJ2f21l6m75dS4Z11d76gidgZfFrxy1BQgjVl7EvJg2xQISvt1efahvCc.png)

This way, when trying to log in, the system verifies that an active session already exists informing the user.

![](/docs/assets/drive/IkC8pMQVLKRCkr3SI1oYDJsaSirmOHxS31Z5ZmwhCzOnMnwXW88ZFHcyTCnp0Vpm9BxY_RJbpWIdrQG0g5DhURD1RSzW2nexd9hGTeCxTNWhaAWaopvCG-r7JieCNHkLjpCb7HW3v3JXDjofFCHEyAU.png)

!!! info
    By default, Etendo with this module installed, only allows to have one session active. 

### **Changing Password after Login**

After logging in for the **first time** with a user, Etendo asks to **change the password**. When trying to log in, the system mentions that the password has expired and that the user needs to change it to a new one to be able to log in.

![](/docs/assets/drive/aJIN1JP1Oau9HSzi_O2NF-rcQBAdE58v59GVg5NoLiQvgTobqai4mOU07aw0D786KJfL0EBJ_rcaQ86-vf8FmZo3gKZnhLaE_yE3Ynzk46CQkhg0abwcMPLKPw2OjUlvFa75h5zkhSW4i97OviTl8mo.png)

Once the change has been made, the user is redirected to the main interface of the application.

### **Expiration Time (Autolock Password)**

As part of the security management, Etendo also allows the management of the days for the **password expiration time**.

From the **Preferences** window, it is possible to adjust the period of time required for the user to be obliged to change the password. Do it by adding the desired amount of days for the password expiration in the **Value** field.

![](/docs/assets/drive/4o5-tsn6u1mWXedVD-rp5GQNpc6RZ6cAroo-BrZc6xPUevOI0COBerM1NnEmySSSMLMBicOBI1Gidh-4D3QkOMPvJI72977qKSYFHtFJ0UtZnChiIcSYi0Nz3Uu_9H5k39FZ7ozJjeyUbxifnWGamz0.png)

!!! info
    Consider that by default, Etendo configures 30 days for the password expiration time. 

After the number of days established for the password expiration, when trying to log in, a message is displayed explaining the need to be redirected to the **login to change the password**, i.e. the user is marked as **password expired**.

Besides, Etendo notifies the user with a message announcing the amount of **remaining days** for the password expiration. In this example, the user has two days left.

![](/docs/assets/drive/0g12hmyWCTy2ecyVLmptMQSLE6ocCBLGSJLJlYa3EqwCNE-NyYSxy-aO9jg88OWefWDsRso8RDce3Zas0q5Q29fUdcrtSeZ-nA13uwNokmr2vnlKM4HabnGCzy5r3stbAmsCoEgMhzno5T6LLr4tyYM.png)

!!! info
    By default, the system activates this message when there are **seven days** left to change the password.