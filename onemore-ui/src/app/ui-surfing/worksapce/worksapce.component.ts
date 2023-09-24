import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { AppCommonComponent } from 'src/app/core/app-common-component';

@Component({
  selector: 'app-worksapce',
  templateUrl: './worksapce.component.html',
  styleUrls: ['./worksapce.component.scss'],
})
export class WorksapceComponent extends AppCommonComponent implements OnInit {
  workspaceList: [any] = [{}];
  workspacePage: [any] = [1];
  workspaceCount = 0;
  currentPage = 1;
  modeOfScreen = 'ENQ';

  formGroup: FormGroup = new FormGroup({
    id: new FormControl(''),
    user: new FormControl(''),
    workspace_name: new FormControl('', [Validators.required]),
    description: new FormControl('', [Validators.required]),
  });
  isCreate: any;

  ngOnInit(): void {
    this.getWorkspace(10, 1);
  }

  /** Get Workspace count */
  getWsCount() {
    this.http
      .post(this.appStoreService.getAipUrl(this.API_WS_COUNT), {})
      .subscribe(
        (response: any) => {
          this.workspaceCount = response.data.count;
          this.workspacePage.pop();
          for (let i = 0; i < response.data.count / 10; i++) {
            this.workspacePage.push(i + 1);
          }
        },
        (error) => {
          this.handleError(error);
        }
      );
  }

  /**Get Workspace for user */
  getWorkspace(perPage: number, page: number) {
    this.http
      .post(this.appStoreService.getAipUrl(this.API__GET_ALL_WORKSPACE), {
        per_page: perPage,
        page: page,
      })
      .subscribe(
        (response: any) => {
          this.workspaceList = response.data;
          this.getWsCount();
        },
        (error) => {
          this.handleError(error);
        }
      );
  }

  saveWorksapce() {
    this.http
      .post(
        this.appStoreService.getAipUrl(this.API__SAVE_WS),
        this.formGroup.getRawValue()
      )
      .subscribe(
        (response: any) => {
          this.notificationService.sendMessage({
            message: 'Workspace saved !',
            type: 0,
          });
          this.modeOfScreen = 'ENQ';
          this.getWorkspace(10, 1);
        },
        (error) => {
          this.handleError(error);
        }
      );
  }

  editWorkspace(ws_id: any) {
    this.http
      .post(this.appStoreService.getAipUrl(this.API_GET_WS), { id: ws_id })
      .subscribe(
        (response: any) => {
          this.modeOfScreen = 'CREATE';
          this.isCreate = false;
          this.formGroup.patchValue(response.data);
        },
        (error) => {
          this.handleError(error);
        }
      );
  }

  updateWorkspace() {
    this.http
      .post(
        this.appStoreService.getAipUrl(this.API_UPDATE_WS),
        this.formGroup.getRawValue()
      )
      .subscribe(
        (response: any) => {
          this.notificationService.sendMessage({
            message: 'Workspace saved !',
            type: 0,
          });
          this.modeOfScreen = 'ENQ';
          this.getWorkspace(10, 1);
        },
        (error) => {
          this.handleError(error);
        }
      );
  }

  manageTS(workspace: any) {
    this.appStoreService.saveCommonVar(this.CONST_WS_ID, workspace.id);
    this.route.navigateByUrl(this.ROUTE_UI_TEST_SUITE);
    localStorage.setItem(this.CONST_WS_ID, workspace.id);
  }
}
