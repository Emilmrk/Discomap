import { Component, OnInit, inject } from '@angular/core'; // Asegúrate de importar OnInit e inject correctamente
import { CommonModule } from '@angular/common';
import { SidebarComponent } from '../sidebar/sidebar.component';
import { MainContentComponent } from '../main-content/main-content.component';
import { FooterComponent } from '../footer/footer.component';
import { AuthService } from '../auth.service';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [
    CommonModule,
    SidebarComponent,
    MainContentComponent,
    FooterComponent
  ],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  isAuthenticated$: Observable<boolean> = of(false);
  username: string | null = null;
  usernameMessage: string = '';

  private authService = inject(AuthService); // Usar inject de @angular/core

  ngOnInit() {
    this.isAuthenticated$ = this.authService.isAuthenticated();
    this.isAuthenticated$.subscribe(isAuthenticated => {
      if (isAuthenticated) {
        this.username = this.authService.getUsername();
        this.usernameMessage = `, ${this.username}`;
      } else {
        this.username = null;
        this.usernameMessage = '';
      }
    });
  }
}
