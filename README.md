# PM-Example
Example PM Plugin for querying Spiget. 


Loona will auto import `PMPlugin` and `PluginQueryResult` when Plugin is loaded

## Documentation
```py
class LoonaPlugin:
    def __init__(self, ...):
        self.name = name
        self.description = description
        self.version = version
        self.author = author
        self.plugin_type = plugin_type
    def log(log_type: int, msg: str) -> None: ...
```
```py
class PMPlugin(LoonaPlugin):
    def query(self, query: str, page: int = 0, limit: int = 25) -> List[PluginQueryResult] | None: ...
    def install(self, install_url: str) -> None: ...
```
```py
class PluginQueryResult(BaseModel):
    id: Any  # Plugin ID
    name: str
    description: Optional[str] = None
    tags: Optional[Union[list, str]] = []  # List of strings
    premium: Optional[bool] = False  # Is the plugin premium? (paid)

    icon: Optional[Union[str, bytes]] = None  # URL or Base64 encoded bytes

    size: Union[int, float]
    views: Optional[int] = 0
    likes: Optional[int] = 0
    downloads: Optional[int] = 0

    versions: Optional[list] = []  # List of strings

    url: str  # URL to the plugin page
    install_url: Optional[str] = None  # URL to the plugin file
    external: Optional[bool] = False  # Install link is on external website?

    releaseDate: Optional[datetime] = None

    service_name: str  # Name of Website or API result is from
```


This repo will obviously be updated
