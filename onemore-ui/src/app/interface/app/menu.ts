export interface OnemoreMenu {
  title: string;
  icon: string;
  route_url: string;
  expand: boolean;
  submenu: [OnemoreMenu];
}
