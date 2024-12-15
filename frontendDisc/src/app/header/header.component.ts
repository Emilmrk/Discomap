import { Component, OnInit } from '@angular/core';
import { SearchService } from '../search.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { AuthService } from '../auth.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {
  isAuthenticated$: Observable<boolean>;
  username: string | null = null;

  constructor(private searchService: SearchService, private authService: AuthService) {
    this.isAuthenticated$ = this.authService.isAuthenticated();
  }

  ngOnInit() {
    this.isAuthenticated$.subscribe(isAuthenticated => {
      if (isAuthenticated) {
        this.username = this.authService.getUsername();
      } else {
        this.username = null;
      }
    });
  }

  onSearch(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.searchService.setSearchTerm(value);
  }

  logout() {
    this.authService.logout();
  }
}
