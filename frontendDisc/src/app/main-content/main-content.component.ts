import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AuthService } from '../auth.service';
import { Observable, of } from 'rxjs';

@Component({
  selector: 'app-main-content',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './main-content.component.html',
  styleUrls: ['./main-content.component.css']
})
export class MainContentComponent implements OnInit {
  isAuthenticated$: Observable<boolean> = of(false); // Inicializa con un valor predeterminado
  username: string | null = null;
  usernameMessage: string = '';

  private authService = inject(AuthService);

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
