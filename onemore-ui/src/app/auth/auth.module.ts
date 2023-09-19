import { NgModule } from "@angular/core";
import { CommonModule } from "@angular/common";
import { OnemoreLoginComponent } from "./onemore-login/onemore-login.component";
import { OnemoreRegisterComponent } from "./onemore-register/onemore-register.component";
import { NbButtonModule, NbInputModule } from "@nebular/theme";
import { FormsModule, ReactiveFormsModule } from "@angular/forms";

@NgModule({
  declarations: [OnemoreLoginComponent, OnemoreRegisterComponent],
  imports: [
    CommonModule,
    NbInputModule,
    NbButtonModule,
    FormsModule,
    ReactiveFormsModule,
  ],
})
export class AuthModule {}
