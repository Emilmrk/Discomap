import { Routes } from '@angular/router';
import { ListaDiscotecasComponent } from './lista-discotecas/lista-discotecas.component';
import { ObjetivoComponent } from './objetivo/objetivo.component';
import { ContactosComponent } from './contactos/contactos.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';  // Asegúrate de importar el componente de registro

export const routes: Routes = [
  { path: '', component: ListaDiscotecasComponent }, // Ruta principal
  { path: 'objetivo', component: ObjetivoComponent },
  { path: 'contactos', component: ContactosComponent },
  { path: 'login', component: LoginComponent }, // Ruta para el login
  { path: 'register', component: RegisterComponent }, // Ruta para el registro
];
