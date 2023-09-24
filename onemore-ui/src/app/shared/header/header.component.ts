import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';
import { AppStoreService } from 'src/app/core/app-store.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss'],
})
export class HeaderComponent {
  userData: any = {};
  constructor(private appStore: AppStoreService, private route: Router) {
    this.userData = appStore.getCommonVar('USER_DATA');
    appStore.USER_DATA.subscribe((data) => {
      this.userData = data;
    });
  }

  logout() {
    localStorage.removeItem('one_token');
    this.route.navigateByUrl('/login');
    this.appStore.SHOW_MENU_S.next(false);
  }
}
