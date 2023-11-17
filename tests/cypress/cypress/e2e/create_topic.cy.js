describe('template spec', () => {
  beforeEach(() => {
    cy.viewport(2048, 1043);

    cy.visit(Cypress.env("CYPRESS_BASE_URL"));
    cy.wait(1000);

    cy.get('#user_code').type(Cypress.env("CYPRESS_USERNAME"));
    cy.wait(1000);

    cy.get('#password').type(
      Cypress.env("CYPRESS_PASSWORD")
    );
    cy.wait(1000);
    cy.get("#login-button").click();
    cy.wait(1000);
    cy.url().should("include", "/home");
  });
  it('passes', () => {
    cy.log("Vamos a crear un topic");
    cy.get("#new-topic-button").click();
    cy.wait(1000);
    cy.get('#title').type("Prueba cypress");
    cy.wait(1000);
    cy.get("#close_date").type("2024-12-30");
    cy.wait(1000);
    cy.get('#group').find('option').first().then(($option) => {
      const valorPrimerElemento = $option.attr('value');
    
      cy.get('#group').select(valorPrimerElemento);
    });
    cy.wait(1000);
    cy.get("#save-topic-button").click();
  })
})