import { Component } from '@angular/core';
import { Spinkit } from 'ng-http-loader';
import { ToastrService } from 'ngx-toastr';
import { AppStoreService } from './core/app-store.service';
import { Router } from '@angular/router';
import { env } from 'src/environment';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'onemore-ui';
  public spinkit = Spinkit;
  showMenu = false;

  constructor(private appStore: AppStoreService, private route: Router) {
    this.subMenu();
  }

  subMenu() {
    this.showMenu = this.appStore.getAuthStatus();
    this.appStore.SHOW_MENU_S.subscribe((data) => {
      if (data) {
        this.showMenu = true;
      } else if (!data) {
        this.showMenu = false;
      }
    });
  }
}
