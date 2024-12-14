import { Component, OnInit } from '@angular/core';
import { DiscotecaService } from '../discoteca.service';
import { SearchService } from '../search.service';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-lista-discotecas',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './lista-discotecas.component.html',
  styleUrls: ['./lista-discotecas.component.css'],
})
export class ListaDiscotecasComponent implements OnInit {
  discotecas: any[] = [];
  filteredDiscotecas: any[] = [];
  selectedDiscoteca: any = null;

  constructor(private discotecaService: DiscotecaService, private searchService: SearchService) {}

  ngOnInit() {
    this.discotecaService.getDiscotecas().subscribe(
      (data) => {
        this.discotecas = data as any[];
        this.filteredDiscotecas = this.discotecas; // Mostrar todas las discotecas inicialmente
        console.log(this.discotecas);
      },
      (error) => {
        console.error('Error al obtener discotecas:', error);
      }
    );

    this.searchService.search$.subscribe(term => {
      this.filterDiscotecas(term);
    });
  }

  toggleDetails(discoteca: any) {
    this.selectedDiscoteca = this.selectedDiscoteca === discoteca ? null : discoteca;
  }

  filterDiscotecas(term: string) {
    term = term.toLowerCase();
    this.filteredDiscotecas = this.discotecas.filter(discoteca =>
      discoteca.nombre.toLowerCase().includes(term) ||
      discoteca.direccion.toLowerCase().includes(term)
    );
  }
}
