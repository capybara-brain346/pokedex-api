pm.test("Response status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Content-Type header is application/json", function () {
  pm.expect(pm.response.headers.get("Content-Type")).to.include(
    "application/json"
  );
});

pm.test("Response time is within an acceptable range", function () {
  pm.expect(pm.response.responseTime).to.be.below(200);
});

pm.test("Validate the structure of the response object", function () {
  const responseData = pm.response.json();

  pm.expect(responseData).to.be.an("object");

  Object.values(responseData).forEach((pokemon) => {
    pm.expect(pokemon.name).to.be.a("string");
    pm.expect(pokemon.type).to.be.a("string");
    pm.expect(pokemon.species).to.be.a("string");
    pm.expect(pokemon.height).to.be.a("number");
    pm.expect(pokemon.weight).to.be.a("number");
    pm.expect(pokemon.abilities).to.be.a("string");
    pm.expect(pokemon.catch_rate).to.be.a("number");
    pm.expect(pokemon.base_friendship).to.be.a("number");
    pm.expect(pokemon.base_exp).to.be.a("number");
    pm.expect(pokemon.growth_rate).to.be.a("string");
    pm.expect(pokemon.gender).to.be.a("string");
    pm.expect(pokemon.hp).to.be.a("number");
    pm.expect(pokemon.attack).to.be.a("number");
    pm.expect(pokemon.defense).to.be.a("number");
    pm.expect(pokemon.sp_attack).to.be.a("number");
    pm.expect(pokemon.sp_defense).to.be.a("number");
    pm.expect(pokemon.speed).to.be.a("number");
  });
});
