---
title: Details 23Q2.0
---
## EPL-493
### Make authentication classes extensible by implementing hooks

**Issue Description**
Make authentication classes `(UserInfoWidgetActionHandler, LoginHandler)` extensible by implementing hooks order to extend and enhance the security functionality

**Solution Design**
Create `UserInfoWidgetHook` and `LoginHandlerHook` for code injection into `UserInfoWidgetActionHandler` and `LoginHandler`.