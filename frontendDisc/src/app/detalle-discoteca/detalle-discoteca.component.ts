import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { DiscotecaService } from '../discoteca.service'; // Verifica la ruta del servicio

@Component({
  selector: 'app-detalle-discoteca',
  standalone: true,
  imports: [CommonModule], // Eliminar HeaderComponent de las importaciones
  templateUrl: './detalle-discoteca.component.html',
  styleUrls: ['./detalle-discoteca.component.css']
})
export class DetalleDiscotecaComponent implements OnInit {
  discoteca: any;
  private route = inject(ActivatedRoute);
  private discotecaService = inject(DiscotecaService);

  ngOnInit() {
    const id = +(this.route.snapshot.paramMap.get('id') ?? 0);
    this.discotecaService.getDiscoteca(id).then(
      (data: any) => {
        this.discoteca = data;
      },
      (error: any) => {
        console.error('Error al obtener detalles de la discoteca:', error);
      }
    );
  }
}
