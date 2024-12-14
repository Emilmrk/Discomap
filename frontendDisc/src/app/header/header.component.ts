import { Component } from '@angular/core';
import { SearchService } from '../search.service';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-header',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  constructor(private searchService: SearchService) {}

  onSearch(event: Event) {
    const value = (event.target as HTMLInputElement).value;
    this.searchService.setSearchTerm(value);
  }
}
