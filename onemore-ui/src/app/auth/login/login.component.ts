import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AppCommonComponent } from 'src/app/core/app-common-component';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent extends AppCommonComponent {
  formGroup: FormGroup = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.min(5)]),
    password: new FormControl('', [Validators.required, Validators.min(5)]),
  });

  loginUser() {
    if (this.formGroup.valid) {
      this.http
        .post(
          this.appStoreService.getAipUrl(this.API_LOGIN),
          this.formGroup.getRawValue()
        )
        .subscribe(
          (response: any) => {
            if (response.status) {
              localStorage.setItem('one_token', response.data.token);
              this.appStoreService.saveCommonVar(
                this.CONST_USER_TOKEN,
                response.data.token
              );
              this.appStoreService.saveCommonVar(this.CONST_USER_DATA, response.data);
              this.appStoreService.userData(response.data);
              this.appStoreService.SHOW_MENU_S.next(true);
              this.route.navigateByUrl(this.ROUTE_ONEMORE);
            }
          },
          (error: Error) => {
            this.handleError(error);
          }
        );
    } else {
      this.formGroup.markAllAsTouched();
    }
  }
}
