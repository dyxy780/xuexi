// k6 性能测试脚本示例
// 位置：软测/k6/login_test.js
// 运行：安装 k6 后，k6 run login_test.js
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  vus: 50,        // 并发虚拟用户数
  duration: '60s' // 持续时间
};

const BASE_URL = __ENV.YOUR_APP_BASE_URL || 'https://reqres.in';

export default function () {
  const url = `${BASE_URL}/api/login`;
  const payload = JSON.stringify({ email: 'eve.holt@reqres.in', password: 'cityslicka' });
  const params = {
    headers: {
      'Content-Type': 'application/json',
    },
  };

  const res = http.post(url, payload, params);
  check(res, {
    'status is 200': (r) => r.status === 200,
    'has token': (r) => r.body.indexOf('token') !== -1,
  });

  sleep(1);
}
