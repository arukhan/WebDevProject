import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Resume } from '../../interfaces/resume';
import { ServiceService } from '../../service/service.service';
import { CommonModule, NgIf, NgFor } from '@angular/common'; 

@Component({
  selector: 'app-resumelist',
  standalone: true,
  templateUrl: './resumelist.component.html',
  styleUrl: './resumelist.component.css',
  imports: [CommonModule, NgIf, NgFor] 
})
export class ResumelistComponent implements OnInit {
  resumes: Resume[] = [];

  constructor(private ser: ServiceService, private router: Router) {}

  ngOnInit(): void {
    this.ser.getResume().subscribe({
      next: (data) => this.resumes = data,
      error: (err) => console.error('Ошибка при получении резюме:', err)
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
