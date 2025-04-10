import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';
import { Vacancy } from '../interfaces/vacancy';
import { Company } from '../interfaces/company';
import { Resume } from '../interfaces/resume';

@Injectable({
  providedIn: 'root'
})
export class ServiceService {
  private accessTokenKey = 'access_token';
  private refreshTokenKey = 'refresh_token';
  private registrationUrl = 'http://127.0.0.1:8000/api/register/'
  private vacanciesUrl = 'http://127.0.0.1:8000/api/vacancy/'
  private companyUrl = 'http://localhost:8000/api/company/'
  private resumeUrl = 'http://localhost:8000/api/resume/'

  constructor(private http: HttpClient) {}

  postRegistration(data: any):Observable<any>{
    const headers = new HttpHeaders(
      {
        'Content-type': 'application/json'
      }
    )
    
    return this.http.post<any>(this.registrationUrl, data, {headers});
  }

  getVacancies():Observable<Vacancy[]>{
    return this.http.get<Vacancy[]>(this.vacanciesUrl)
  }

  getResume():Observable<Resume[]>{
    return this.http.get<Resume[]>(this.resumeUrl)
  }

  getCompanies():Observable<Company[]>{
    return this.http.get<Company[]>(this.companyUrl)
  }


  login(username: string, password: string) {
    return this.http.post<any>('http://localhost:8000/api/token/', { username, password });
  }

  saveTokens(access: string, refresh: string) {
    localStorage.setItem(this.accessTokenKey, access);
    localStorage.setItem(this.refreshTokenKey, refresh);
  }

  getAccessToken(): string | null {
    return localStorage.getItem(this.accessTokenKey);
  }

  getRefreshToken(): string | null {
    return localStorage.getItem(this.refreshTokenKey);
  }

  updateAccessToken(refresh: string) {
    return this.http.post<any>('http://localhost:8000/api/token/refresh/', { refresh });
  }

  logout() {
    localStorage.removeItem(this.accessTokenKey);
    localStorage.removeItem(this.refreshTokenKey);
  }



}
