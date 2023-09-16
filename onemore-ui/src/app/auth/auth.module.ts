import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { LoginComponent } from './login/login.component';
import { CreateUserComponent } from './create-user/create-user.component';



@NgModule({
  declarations: [
    LoginComponent,
    CreateUserComponent
  ],
  imports: [
    CommonModule
  ]
})
export class AuthModule { }
