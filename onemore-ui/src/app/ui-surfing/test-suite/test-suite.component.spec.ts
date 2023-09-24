import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TestSuiteComponent } from './test-suite.component';

describe('TestSuiteComponent', () => {
  let component: TestSuiteComponent;
  let fixture: ComponentFixture<TestSuiteComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TestSuiteComponent]
    });
    fixture = TestBed.createComponent(TestSuiteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
