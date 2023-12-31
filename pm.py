"""
https://loona.gg
"""

import urllib.parse
from typing import List, Union, Tuple

import requests


class SpigotManager(PMPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.WEBSITE_URL = "https://www.spigotmc.org/"
        self.API_ENDPOINT = "https://api.spiget.org/v2/"
        self.DEFAULT_EXT = "jar"

    def query(self, query: str, page: int = 0, limit: int = 25) -> Union[List[PluginQueryResult] | None, Tuple[List[PluginQueryResult], int] | None]:
        """
        Called when user is searching for a Plugin
        :param query: User search query
        :param page: Returned Page
        :param limit: Items per page
        :return: List[QueryResult] | None
        """
        query = urllib.parse.quote(query)
        url = f"{self.API_ENDPOINT}search/resources/{query}?size={limit}&page={page}"
        print(url)
        r = requests.get(url)
        if r.status_code == 200:
            js = r.json()
            results = []
            for result in js:
                results.append(PluginQueryResult(
                    id=result["id"],
                    filename=f"{result['id']}.jar",
                    name=result["name"],
                    description=result["tag"] if "tag" in result else "",
                    tags=[],
                    premium=result["premium"] if "premium" in result else False,
                    icon=result["icon"]["data"] if result["icon"]["data"] else None,
                    size=int(result["file"]["size"]) * 1000,  # Convert to bytes
                    views=result["views"] if "views" in result else 0,
                    likes=result["likes"] if "likes" in result else 0,
                    downloads=result["downloads"] if "downloads" in result else 0,
                    versions=result["testedVersions"] if "testedVersions" in result else [],
                    url=self.WEBSITE_URL + result["file"]["url"],
                    install_url=self.API_ENDPOINT + "resources/" + str(result["id"]) + "/download",
                    external=result["external"],
                    releaseDate=result["releaseDate"],
                    service_name="SpigotMC"
                ))
            return results
        else:
            return []

    def get_plugin(self, plugin_id: Union[str, int]) -> PluginQueryResult:
        """
        Called when plugin is being installed
        :param plugin_id: Plugin ID
        :return: PluginQueryResult
        """
        url = f"{self.API_ENDPOINT}resources/{plugin_id}"
        r = requests.get(url)
        if r.status_code == 200:
            result = r.json()
            return PluginQueryResult(
                id=result["id"],
                filename=f"{result['id']}.jar",
                name=result["name"],
                description=result["tag"] if "tag" in result else "",
                tags=[],
                premium=result["premium"] if "premium" in result else False,
                icon=result["icon"]["data"] if result["icon"]["data"] else None,
                size=int(result["file"]["size"]) * 1000,  # Convert to bytes
                views=result["views"] if "views" in result else 0,
                likes=result["likes"] if "likes" in result else 0,
                downloads=result["downloads"] if "downloads" in result else 0,
                versions=result["testedVersions"] if "testedVersions" in result else [],
                url=self.WEBSITE_URL + result["file"]["url"],
                install_url=self.API_ENDPOINT + "resources/" + str(result["id"]) + "/download",
                external=result["external"],
                releaseDate=result["releaseDate"],
                service_name="SpigotMC"
            )
        else:
            return None

    def install(self, plugin: PluginQueryResult, server: str) -> None:
        """
        Called after plugin is installed
        :param plugin: PluginQueryResult
        :param server: UUID of server
        :return: None
        """
        self.log(1, f"Plugin {plugin.name} (ID: {plugin.id}) was installed on {server}")


def setup(*args, **kwargs):
    """Called to load plugin - MUST RETURN THE PLUGIN CLASS"""
    return SpigotManager(*args, **kwargs)
