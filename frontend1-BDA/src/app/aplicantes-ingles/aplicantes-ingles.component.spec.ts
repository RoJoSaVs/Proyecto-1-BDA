import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AplicantesInglesComponent } from './aplicantes-ingles.component';

describe('AplicantesInglesComponent', () => {
  let component: AplicantesInglesComponent;
  let fixture: ComponentFixture<AplicantesInglesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AplicantesInglesComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(AplicantesInglesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
