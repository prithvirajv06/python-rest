import { ChangeDetectorRef, Component } from "@angular/core";
import { Router } from "@angular/router";
import {
  NbAuthService,
  NbAuthSocialLink,
  NbLoginComponent,
} from "@nebular/auth";

@Component({
  selector: "ngx-onemore-login",
  templateUrl: "./onemore-login.component.html",
  styleUrls: ["./onemore-login.component.scss"],
})
export class OnemoreLoginComponent {
  protected service: NbAuthService;
  protected options: {};
  protected cd: ChangeDetectorRef;
  protected router: Router;
  redirectDelay: number;
  showMessages: any;
  strategy: string;
  errors: string[] = [];
  messages: string[];
  user: any = {};
  submitted: boolean;
  socialLinks: NbAuthSocialLink[];
  rememberMe: boolean;
  login() {}
}
