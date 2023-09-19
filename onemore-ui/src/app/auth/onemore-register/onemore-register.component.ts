import { ChangeDetectorRef, Component } from "@angular/core";
import { Router } from "@angular/router";
import { NbAuthService, NbAuthSocialLink } from "@nebular/auth";

@Component({
  selector: "ngx-onemore-register",
  templateUrl: "./onemore-register.component.html",
  styleUrls: ["./onemore-register.component.scss"],
})
export class OnemoreRegisterComponent {
  constructor() {}

  protected service: NbAuthService;
  protected options: {};
  protected cd: ChangeDetectorRef;
  protected router: Router;
  redirectDelay: number;
  showMessages: any;
  strategy: string;
  submitted: boolean;
  errors: string[];
  messages: string[];
  user: any = {};
  socialLinks: NbAuthSocialLink[];

  register() {}
}
