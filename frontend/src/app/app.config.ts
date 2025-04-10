import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { HttpInterceptor } from '@angular/common/http';
import { interceptorInterceptor } from './interceptor/interceptor.interceptor';
import { provideHttpClient } from '@angular/common/http';
import { withInterceptors } from '@angular/common/http';

import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideZoneChangeDetection({ eventCoalescing: true }), provideRouter(routes), provideHttpClient(withInterceptors([interceptorInterceptor]))]
};
