"""File contains zapper integration"""
import aiohttp
from config import Config
from pydantic import Json


class ZapperIntegration:
    """Class contains zapper integration"""

    api_key: str
    base_url: str
    headers: dict
    session: aiohttp.ClientSession

    def __init__(self) -> None:
        self.api_key = Config.Integrations.zapper_api_key
        self.base_url = 'https://api.zapper.xyz/api'
        self.headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.api_key
        }
        self.session = aiohttp.ClientSession()
        self.available_networks = [
            "ethereum", "polygon", "optimism", "gnosis",
            "binance-smart-chain", "fantom", "avalanche",
            "arbitrum", "celo", "moonriver", "bitcoin", "aurora"
        ]
        self.supported_networks = ["ethereum"]

    # ? Wallet specific actions
    async def balances_apps(self, addresses: list[str], networks: list[str] = None, use_cache: bool = True) -> Json:
        if networks is None:
            networks = self.supported_networks

        url = f"{self.base_url}/v2/balances/apps"

        if use_cache:
            async with self.session.get(url, headers=self.headers) as response:
                return await response.json()

        else:
            parameters: dict
            async with self.session.post(url, headers=self.headers) as response:
                parameters = {
                    'jobId': await response.json()['job_id']
                }
            async with self.session.get(url, parameters=parameters, headers=self.headers) as response:
                return await response.json()


    async def balances_tokens(self, addresses: list[str], networks: list[str] = None) -> Json:
        if networks is None:
            networks = self.supported_networks

        url = f"{self.base_url}/v2/balances/tokens"
        raise NotImplementedError

    async def balances_job_status(self, job_id: str) -> Json:
        url = f"{self.base_url}/v2/balances/job-status"
        async with self.session.get(url, headers=self.headers) as response:
            return await response.json()

    async def balances_app(self, app_slug: str) -> Json:
        url = f"{self.base_url}/v2/apps/{app_slug}/balances"
        raise NotImplementedError

    async def balances_apps_supported(self) -> Json:
        url = f"{self.base_url}/v2/apps/balances/supported"
        raise NotImplementedError

    # ? Apps actions
    async def get_app(self, app_slug: str) -> Json:
        url = f"{self.base_url}/v2/apps/{app_slug}/balances"
        raise NotImplementedError

    async def get_apps(self) -> Json:
        url = f"{self.base_url}/v2/apps"
        raise NotImplementedError

    async def get_app_tokens(self, app_id: str) -> Json:
        url = f"{self.base_url}/v2/apps/{app_id}/tokens"
        raise NotImplementedError

    async def get_app_positions(self, app_id: str) -> Json:
        url = f"{self.base_url}/v2/apps/{app_id}/positions"
        raise NotImplementedError

    # ? NFT actions
    async def nft_net_worth(self) -> Json:
        url = f"{self.base_url}/v2/nft/balances/net-worth"
        raise NotImplementedError

    async def nft_user_tokens(self) -> Json:
        url = f"{self.base_url}/v2/nft/user/tokens"
        raise NotImplementedError

    async def nft_balances_tokens(self) -> Json:
        url = f"{self.base_url}/v2/nft/balances/tokens"
        raise NotImplementedError

    async def nft_balances_collections(self) -> Json:
        url = f"{self.base_url}/v2/nft/balances/collections"
        raise NotImplementedError

    async def nft_balances_collections_total(self) -> Json:
        url = f"{self.base_url}/v2/nft/balances/collections-total"
        raise NotImplementedError

    async def nft_tokens_totals(self) -> Json:
        url = f"{self.base_url}/v2/nft/balances/tokens-total"
        raise NotImplementedError

    # ? Misc actions
    async def get_prices(self) -> Json:
        url = f"{self.base_url}/v2/exchange/price"
        raise NotImplementedError

    async def get_gas_prices(self) -> Json:
        url = f"{self.base_url}/v2/exchange/gas-prices"
        raise NotImplementedError

    async def get_api_points(self) -> Json:
        """Returns available api points left in Zapper account"""
        url = f"{self.base_url}/v2/api-clients/points"
        async with self.session.get(url, headers=self.headers) as response:
            return await response.json()
