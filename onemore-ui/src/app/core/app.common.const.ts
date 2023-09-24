export class RouteConst {
  public ROUTE_LOGIN = '/login';
  public ROUTE_ONEMORE = '/onemore';
  public ROUTE_DASHBOARD = '/onemore/dash-board';
  public ROUTE_UI_WORKSPACE = '/onemore/ui-workspace';
  public ROUTE_UI_TEST_SUITE = '/onemore/ui-testsuite';
  public ROUTE_API_WORKSPACE = '/onemore/APi-worksapce';
}

export class CommonConst extends RouteConst {
  constructor() {
    super();
  }
  public CONST_USER_TOKEN = 'USER_TOKEN';
  public CONST_USER_DATA = 'USER_DATA';
  public CONST_WS_ID = 'WS_ID';

  public API_LOGIN = 'login';
  public API_REGISTER = 'register';

  public API__GET_ALL_WORKSPACE = 'get-all-my-ws';
  public API_WS_COUNT = 'get-ws-count';
  public API__SAVE_WS = 'save-ws';
  public API_UPDATE_WS = 'update-ws';
  public API_GET_WS = 'get-ws';

  public API_GET_ALL_TEST_SUITE = 'get-all-test-suite';
  public API_SAVE_TEST_SUITE = 'save-test-suite';
  public API_DELETE_TEST_SUITE = 'delete-test-suite';

  public API_GET_ALL_TEST_CASE = 'get-all-tc';
  public API_SAVE_TEST_CASE = 'save-all-tc';
  public API_DELETE_TEST_CASE = 'delete-tc';
  public API_UPDATE_TEST_CASE = 'update-test-case';
  public API_GET_TEST_CASE = 'get-test-case';
}
