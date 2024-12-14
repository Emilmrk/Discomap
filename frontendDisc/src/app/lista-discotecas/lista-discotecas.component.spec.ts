import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListaDiscotecasComponent } from './lista-discotecas.component';

describe('ListaDiscotecasComponent', () => {
  let component: ListaDiscotecasComponent;
  let fixture: ComponentFixture<ListaDiscotecasComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ListaDiscotecasComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListaDiscotecasComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
