import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'asset-register-management',
    pathMatch: 'full'
  },
  // {
  //   path: 'asset-register-management',
  //   loadChildren: () => import('./asset-list/asset-list.module').then( m => m.AssetListPageModule)
  // },
  {
    path: 'asset-makes',
    loadChildren: () => import('./asset-makes/asset-makes.module').then( m => m.AssetMakesPageModule)
  },
  {
    path: 'asset-models',
    loadChildren: () => import('./asset-models/asset-models.module').then( m => m.AssetModelsPageModule)
  },
  {
    path: 'asset-types',
    loadChildren: () => import('./asset-types/asset-types.module').then( m => m.AssetTypesPageModule)
  },
  {
    path: 'vendors',
    loadChildren: () => import('./vendors/vendors.module').then( m => m.VendorsPageModule)
  },
  {
    path: 'offices',
    loadChildren: () => import('./offices/offices.module').then( m => m.OfficesPageModule)
  },
  {
    path: 'asset-owners',
    loadChildren: () => import('./asset-owners/asset-owners.module').then( m => m.AssetOwnersPageModule)
  }
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
