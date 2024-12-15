import { Routes } from '@angular/router';
import { ListaDiscotecasComponent } from './lista-discotecas/lista-discotecas.component';
import { ObjetivoComponent } from './objetivo/objetivo.component';
import { ContactosComponent } from './contactos/contactos.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component'; // Importa el nuevo componente
import { DetalleDiscotecaComponent } from './detalle-discoteca/detalle-discoteca.component'; // Importa el nuevo componente

export const routes: Routes = [
  { path: '', component: HomeComponent }, // Ruta principal
  { path: 'objetivo', component: ObjetivoComponent },
  { path: 'contactos', component: ContactosComponent },
  { path: 'login', component: LoginComponent }, // Ruta para el login
  { path: 'register', component: RegisterComponent }, // Ruta para el registro
  { path: 'discotecas', component: ListaDiscotecasComponent }, // Ruta para la lista de discotecas
  { path: 'discotecas/:id', component: DetalleDiscotecaComponent }, // Ruta para detalles de discotecas
];