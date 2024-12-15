import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { firstValueFrom } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DiscotecaService {
  private discotecasUrl = 'http://localhost:8000/api/discotecas/'; // URL del endpoint de discotecas en Django

  constructor(private http: HttpClient) { }

  getDiscotecas(): Promise<any> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Token ${token}`);
    return firstValueFrom(this.http.get<any>(this.discotecasUrl, { headers }));
  }

  getDiscoteca(id: number): Promise<any> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Token ${token}`);
    return firstValueFrom(this.http.get<any>(`${this.discotecasUrl}${id}/`, { headers }));
  }

  createDiscoteca(discoteca: any): Promise<any> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Token ${token}`);
    return firstValueFrom(this.http.post<any>(this.discotecasUrl, discoteca, { headers }));
  }

  updateDiscoteca(id: number, discoteca: any): Promise<any> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Token ${token}`);
    return firstValueFrom(this.http.put<any>(`${this.discotecasUrl}${id}/`, discoteca, { headers }));
  }

  deleteDiscoteca(id: number): Promise<any> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders().set('Authorization', `Token ${token}`);
    return firstValueFrom(this.http.delete<any>(`${this.discotecasUrl}${id}/`, { headers }));
  }
}
