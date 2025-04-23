import { Component, OnInit } from '@angular/core';
import { Company } from '../../interfaces/company';
import { ServiceService } from '../../service/service.service';
import { CommonModule, NgIf, NgFor } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-companylist',
  standalone: true,
  imports: [CommonModule, NgFor, FormsModule],
  templateUrl: './companylist.component.html',
  styleUrl: './companylist.component.css'
})
export class CompanylistComponent implements OnInit {
  companies: Company[] = [];

  constructor(private service: ServiceService, private router: Router) {}

  ngOnInit(): void {
    this.service.getCompanies().subscribe({
      next: (data) => this.companies = data,
      error: (err) => console.error('Ошибка при получении компании', err)
    });
  }

  goHome() {
    this.router.navigate(['/protected']);
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    this.router.navigate(['/login']);
  }
}
