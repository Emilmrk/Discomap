import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RegisterService {
  private registerUrl = 'http://localhost:8000/api/usuarios/register/';  // URL del endpoint de registro en Django

  constructor(private http: HttpClient) { }

  register(username: string, password: string): Observable<any> {
    return this.http.post<any>(this.registerUrl, { username, password });
  }
}
