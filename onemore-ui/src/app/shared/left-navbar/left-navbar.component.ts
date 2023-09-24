import { Component, OnInit } from '@angular/core';
import { AppStoreService } from 'src/app/core/app-store.service';
import { OnemoreMenu } from 'src/app/interface/app/menu';

@Component({
  selector: 'app-left-navbar',
  templateUrl: './left-navbar.component.html',
  styleUrls: ['./left-navbar.component.scss'],
})
export class LeftNavbarComponent implements OnInit {
  menu_data!: [OnemoreMenu];
  constructor(private app_store_service: AppStoreService) {}

  ngOnInit(): void {
    this.menu_data=this.app_store_service.MENU_BS.getValue();
    this.app_store_service.MENU_BS.subscribe((menu_data_sub) => {
      this.menu_data = menu_data_sub;
    });
  }
}
