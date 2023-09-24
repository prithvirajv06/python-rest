import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HeaderComponent } from './header/header.component';
import { LeftNavbarComponent } from './left-navbar/left-navbar.component';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';

@NgModule({
  declarations: [HeaderComponent, LeftNavbarComponent],
  imports: [CommonModule, HttpClientModule, RouterModule],
  exports: [HeaderComponent, LeftNavbarComponent],
})
export class SharedModule {}
