import { Component } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { AppCommonComponent } from 'src/app/core/app-common-component';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent extends AppCommonComponent {
  confirmPassMismatch = false;
  formGroup: FormGroup = new FormGroup({
    username: new FormControl('', []),
    email: new FormControl('', [Validators.required, Validators.min(5)]),
    password: new FormControl('', [Validators.required, Validators.min(5)]),
    confirmPassword: new FormControl('', [Validators.required]),
  });

  registerUser() {
    if (this.formGroup.valid) {
      if (
        this.formGroup.get('password')?.value !=
        this.formGroup.get('confirmPassword')?.value
      ) {
        this.confirmPassMismatch = true;
        return;
      }
      this.formGroup.patchValue({
        username: this.formGroup.getRawValue().email,
      });
      this.http
        .post(
          this.appStoreService.getAipUrl(this.API_REGISTER),
          this.formGroup.getRawValue()
        )
        .subscribe(
          (response: any) => {
            if (response.status) {
              this.route.navigateByUrl(this.ROUTE_LOGIN);
            }
          },
          (error: any) => {
            this.handleError(error);
          }
        );
    } else {
      this.notificationService.sendMessage({
        message: 'Clear all errors !',
        type: 1,
      });
      this.formGroup.markAllAsTouched();
    }
  }
}
