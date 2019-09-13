# :rocket: snapi-launch-notif-server

Snapi is originally a project by u/[derkweijers](https://github.com/derkweijers) under the
[spaceflightnewsapi](https://github.com/spaceflightnewsapi) project.

This repo pertains to updating the notification server's launch collection.

## Setup for Dev Instance

:package: Install mongodb locally as per the [instructions](https://docs.mongodb.com/manual/installation/).

- Create a db using the `use` keyword in the mongo shell

```mongo
> use snapi
```

- View your collections

```mongo
> db.collections
```

- To create a new collection use

```
> db.createCollection('launchnotifications')
```