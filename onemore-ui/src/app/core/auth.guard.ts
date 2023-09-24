import { Injectable } from "@angular/core";
import {
	ActivatedRouteSnapshot,
	CanActivate,
	Router,
	RouterStateSnapshot,
	UrlTree
} from "@angular/router";
import { AppStoreService } from "./app-store.service";

@Injectable()
export class AuthGuard implements CanActivate {
	constructor(
		private authService: AppStoreService,
		private router: Router) { }
	canActivate(
		route: ActivatedRouteSnapshot,
		state: RouterStateSnapshot): boolean | Promise<boolean> {
		var isAuthenticated = this.authService.getAuthStatus();
		if (!isAuthenticated) {
			this.router.navigate(['/login']);
		}
		return isAuthenticated;
	}
}
