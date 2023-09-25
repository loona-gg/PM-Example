"""
Made by https://artucuno.dev for Loona.gg
"""

import urllib.parse
from typing import List, Union, Tuple

import requests


class MyPlugin(PMPlugin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.WEBSITE_URL = "https://www.spigotmc.org/"
        self.API_ENDPOINT = "https://api.spiget.org/v2/"

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
        r = requests.get(url)
        if r.status_code == 200:
            js = r.json()
            results = []
            for result in js:
                results.append(PluginQueryResult(
                    id=result["id"],
                    name=result["name"],
                    description=result["description"] if "description" in result else None,
                    tags=result["tag"],
                    premium=result["premium"] if "premium" in result else False,
                    icon=result["icon"]["data"],
                    size=result["file"]["size"],
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

    def install(self, plugin: PluginQueryResult, server: str) -> None:
        """
        Called after plugin is installed
        :param plugin: PluginQueryResult
        :param server: UUID of server
        :return: None
        """
        self.log(1, f"Plugin {plugin.name} (ID: {plugin.id}) was installed to {server}")


def setup(*args, **kwargs):
    """Called to load plugin - MUST RETURN PLUGIN CLASS"""
    return PM(*args, **kwargs)

