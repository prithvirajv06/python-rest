import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WorksapceComponent } from './worksapce.component';

describe('WorksapceComponent', () => {
  let component: WorksapceComponent;
  let fixture: ComponentFixture<WorksapceComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [WorksapceComponent]
    });
    fixture = TestBed.createComponent(WorksapceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
