import { ExtraOptions, RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';
import {
  NbAuthComponent,
  NbLoginComponent,
  NbLogoutComponent,
  NbRegisterComponent,
  NbRequestPasswordComponent,
  NbResetPasswordComponent,
} from '@nebular/auth';
import { OnemoreLoginComponent } from './auth/onemore-login/onemore-login.component';
import { OnemoreRegisterComponent } from './auth/onemore-register/onemore-register.component';

export const routes: Routes = [
  // {
  //   path: 'pages',
  //   loadChildren: () => import('./pages/pages.module')
  //     .then(m => m.PagesModule),
  // },
  {
    path: 'auth',
    component: NbAuthComponent,
    children: [
      {
        path: '',
        component: NbLoginComponent,
      },
      {
        path: 'login',
        component: OnemoreLoginComponent,
      },
      {
        path: 'register',
        component: OnemoreRegisterComponent,
      }
    ],
  },
  { path: '', redirectTo: 'auth', pathMatch: 'full' },
  { path: '**', redirectTo: 'pages' },
];

const config: ExtraOptions = {
  useHash: false,
};

@NgModule({
  imports: [RouterModule.forRoot(routes, config)],
  exports: [RouterModule],
})
export class AppRoutingModule {
}
