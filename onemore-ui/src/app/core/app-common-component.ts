import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { AppStoreService } from './app-store.service';
import { CommonConst } from './app.common.const';
import { Router } from '@angular/router';
import { NotificationService } from './notication-toast/notification.service';

@Component({
  selector: 'app-common-root',
  template: '',
})
export class AppCommonComponent extends CommonConst {
  title = 'onemore-ui';

  constructor(
    public http: HttpClient,
    public appStoreService: AppStoreService,
    public route: Router,
    public notificationService: NotificationService
  ) {
    super();
  }

  handleError(error: any) {
    if (error.status == 401) {
      this.route.navigateByUrl(this.ROUTE_LOGIN);
      localStorage.clear();
      this.appStoreService.SHOW_MENU_S.next(false);
    }
    if (error.status == 500) {
      this.notificationService.sendMessage({
        message: 'Something wrong please report !',
        type: 2,
      });
    } else {
      for (let err of error.error.message) {
        this.notificationService.sendMessage({
          message: err.error,
          type: 2,
        });
      }
    }
  }
}
