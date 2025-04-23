import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { inject } from '@angular/core';
import { Router, RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { NgIf } from '@angular/common';
@Component({
  selector: 'app-protected',
  imports: [CommonModule, RouterModule, NgIf],
  templateUrl: './protected.component.html',
  styleUrl: './protected.component.css'
})
export class ProtectedComponent {
  message = '';
  private http = inject(HttpClient);
  private router = inject(Router)
  constructor() {
    this.http.get<any>('http://localhost:8000/api/protected/').subscribe({
      next: (data) => this.message = data.message,
      error: () => {
        this.message = 'Access denied or token invalid',
        this.router.navigate(['/login']);
    },
  });
}
}
