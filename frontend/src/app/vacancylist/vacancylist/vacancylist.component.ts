import { Component, OnInit } from '@angular/core';
import { Vacancy } from '../../interfaces/vacancy';
import { ServiceService } from '../../service/service.service';
import { NgFor, NgIf } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-vacancylist',
  imports: [NgFor, NgIf, FormsModule],
  templateUrl: './vacancylist.component.html',
  styleUrl: './vacancylist.component.css'
})
export class VacancylistComponent implements OnInit {
  vacancies: Vacancy[] = [];

  constructor(private ser: ServiceService, private router: Router) {}

  ngOnInit(): void {
    this.ser.getVacancies().subscribe({
      next: (data) => this.vacancies = data,
      error: (err) => console.error('Ошибка при получении вакансии', err)
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
