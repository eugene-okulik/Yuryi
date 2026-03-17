from playwright.sync_api import Page, Route
import re
import json


def test_modify_specific_api(page: Page):
    print("\n" + "=" * 70)
    print("ТЕСТ ПЕРЕХВАТА ЗАПРОСОВ")
    print("=" * 70)

    def change_req(route: Route):
        response = route.fetch()
        print(response)
        print(f"\n🎯 Перехвачен API запрос:")
        print(f"{route.request.url}")
        try:
            data = response.json()
            modified = json.loads(json.dumps(data).replace('iPhone', 'Яблокофон'))
            route.fulfill(
                response=response,
                json=modified
            )
        except:
            route.fulfill(response=response)

    page.route(re.compile(r'.*(api|\.json).*'), change_req)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.wait_for_timeout(3000)

    page.locator('.rf-hcard-copy').first.click()
    page.wait_for_timeout(3000)
    header = page.locator('.rf-digitalmat-overlay-header').first.inner_text()
    print(f"\n📦 Заголовок: {header}")
    print("=" * 70 + "\n")
