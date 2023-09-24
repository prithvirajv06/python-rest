import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { BehaviorSubject, Subject } from 'rxjs';
import { OnemoreMenu } from '../interface/app/menu';
import { CommonConst } from './app.common.const';

@Injectable({
  providedIn: 'root',
})
export class AppStoreService {
  COMMON_VARS: any = {};
  MENU_BS: BehaviorSubject<any> = new BehaviorSubject({});
  ENV_JSON_BS: BehaviorSubject<any> = new BehaviorSubject({});
  SHOW_MENU_S: BehaviorSubject<boolean> = new BehaviorSubject(false);
  USER_DATA: BehaviorSubject<{}> = new BehaviorSubject({});
  REFRESH_TS: Subject<any> = new Subject();
  constructor(private http: HttpClient) {
    this.loadMenu();
    this.getEnvJson();
  }

  private loadMenu() {
    this.http.get('/assets/json/menu.json').subscribe((menu_res: any) => {
      let _menu: [OnemoreMenu] = menu_res.TESTER;
      this.MENU_BS.next(_menu);
    });
  }

  private getEnvJson() {
    this.http.get('/assets/json/env.json').subscribe((env_res: any) => {
      let _envJson: [OnemoreMenu] = env_res;
      this.ENV_JSON_BS.next(_envJson);
    });
  }

  public getAipUrl(_urlKey: string) {
    let _envJson: any = this.ENV_JSON_BS.getValue();
    return _envJson['base_url'] + _envJson['api'][_urlKey];
  }

  public saveCommonVar(_key: string, _value: string) {
    this.COMMON_VARS[_key] = _value;
  }

  public getCommonVar(_key: string) {
    return this.COMMON_VARS[_key];
  }

  public userData(data: any) {
    this.USER_DATA.next(data);
  }

  getAuthStatus() {
    return localStorage.getItem('one_token') ? true : false;
  }
}
