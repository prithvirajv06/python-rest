import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SharedModule } from './shared/shared.module';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { ToastrModule } from 'ngx-toastr';
import { NgHttpLoaderModule } from 'ng-http-loader';
import { AuthModule } from './auth/auth.module';
import { CoreModule } from './core/core.module';
import { AppStoreService } from './core/app-store.service';
import { AuthInterceptor } from './core/interceptors/token.interceptor';

@NgModule({
  declarations: [AppComponent],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot(),
    NgHttpLoaderModule.forRoot(),
    AppRoutingModule,
    SharedModule,
    CoreModule,
    HttpClientModule,
    AuthModule,
  ],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
  ],
  bootstrap: [AppComponent],
})
export class AppModule {}
