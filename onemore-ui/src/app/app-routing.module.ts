import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppStoreService } from './core/app-store.service';
import { LoginComponent } from './auth/login/login.component';
import { RegisterComponent } from './auth/register/register.component';
import { AuthGuard } from './core/auth.guard';

const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  {
    path: 'onemore',
    loadChildren: () =>
      import('../app/ui-surfing/ui-surfing.module').then(
        (m) => m.UiSurfingModule
      ),
    canActivate: [AuthGuard],
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
  providers: [AppStoreService, AuthGuard],
})
export class AppRoutingModule {}
