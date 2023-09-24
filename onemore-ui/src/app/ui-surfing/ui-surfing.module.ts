import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WorksapceComponent } from './worksapce/worksapce.component';
import { TestSuiteComponent } from './test-suite/test-suite.component';
import { TestCaseComponent } from './test-case/test-case.component';
import { RouterModule, Routes } from '@angular/router';
import { CoreModule } from '../core/core.module';
const route: Routes = [
  { path: '', redirectTo: 'ui-workspace', pathMatch: 'full' },
  { path: 'ui-workspace', component: WorksapceComponent },
  { path: 'ui-testsuite', component: TestSuiteComponent},
];

@NgModule({
  declarations: [WorksapceComponent, TestSuiteComponent, TestCaseComponent],
  imports: [CommonModule, RouterModule.forChild(route), CoreModule],
})
export class UiSurfingModule {}
