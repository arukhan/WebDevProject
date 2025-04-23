import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { CommonModule, NgIf } from '@angular/common';

@Component({
  selector: 'app-protected',
  imports: [CommonModule, RouterModule, FormsModule, NgIf],
  templateUrl: './protected.component.html',
  styleUrl: './protected.component.css'
})
export class ProtectedComponent {
  message = '';
  private http = inject(HttpClient);
  private router = inject(Router);

  constructor() {
    this.http.get<any>('http://localhost:8000/api/protected/').subscribe({
      next: (data) => this.message = data.message,
      error: () => {
        this.message = 'Access denied or token invalid';
        this.router.navigate(['/login']);
      },
    });
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.router.navigate(['/login']);
  }

  goTo(path: string) {
    this.router.navigate([path]);
  }
  searchQuery = '';
searchResults: any[] = [];

companies: any[] = [];
vacancies: any[] = [];

ngOnInit(): void {
  this.fetchAll();
}

fetchAll() {
  this.http.get<any[]>('http://localhost:8000/api/company/').subscribe(data => this.companies = data);
  this.http.get<any[]>('http://localhost:8000/api/vacancy/').subscribe(data => this.vacancies = data);
}

search() {
  const query = this.searchQuery.toLowerCase().trim();

  this.searchResults = [];

  const foundCompanies = this.companies.filter(c => c.name.toLowerCase().includes(query)).map(c => ({
    type: 'company',
    name: c.name
  }));

  const foundVacancies = this.vacancies.filter(v => v.name.toLowerCase().includes(query)).map(v => ({
    type: 'vacancy',
    name: v.name
  }));

  this.searchResults = [...foundCompanies, ...foundVacancies];
}

}
